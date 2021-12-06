import sys
import re
import string

class Theater:
    # Create a theater with the given parameters for size and buffer for public safety 
    def __init__(self, rows, seats, bufer_seats, bufer_row):
        if seats < 1 or rows < 1 or bufer_seats < 0 or bufer_row < 0:
            print("Invalid theater parameter")
            sys.exit()

        self.seats_per_row = seats
        self.seats_per_row_char = list(string.ascii_uppercase)[0:seats]

        self.bufer_seats = bufer_seats
        
        # Rows that are 2/3 of the way back
        # then move forward from center toward the screen with the given theater size.
        # self.row_priority[i] = [i, #seat_available, start_index of seat_available]
        self.row_priority = []
        row_step  = bufer_row + 1
        for row in range(((rows * 2) / 3) - 1, rows, row_step):
            self.row_priority.append([row, seats, 0])
        for row in range(((rows * 2) / 3) - 3, 0, -row_step):
            self.row_priority.append([row, seats, 0])
    
    # Seat allocation 
    def allocate_seat(self, seats_requested):
        seats_reserved = []
        
        # Find a row that have enough seats for the party
        for i in range(0, len(self.row_priority)):
            row = self.row_priority[i][0]
            seat_available = self.row_priority[i][1]
            if seat_available >= seats_requested:
                start_index = self.row_priority[i][2]
                end_index = start_index + seats_requested

                 # Assign seat
                for col in range(start_index, end_index):
                    seat = self.seats_per_row_char[row] + str(col + 1)
                    seats_reserved.append(seat)
                
                # Update the leftover seats and index for the next allocation after buffered
                self.row_priority[i][1] -= seats_requested + self.bufer_seats
                next_allocation = end_index + self.bufer_seats
                if next_allocation > self.seats_per_row - 1:
                    self.row_priority.pop(0)
                else:
                    self.row_priority[i][2] = next_allocation
                
                break
        
        # Return the location of seats assigned or announce if there is not enough seats available 
        if len(seats_reserved) == 0:
            return "Not enough seats available for the party in this show."
        return ', '.join(seats_reserved)
            
def main():
    if len(sys.argv) != 2:
        print("The program should accept only path to the input file as an argument.")
        sys.exit()

    input_path = sys.argv[1]
    try:
        input_file = open(input_path)
    except IOError:
        print("Input file does not exist.")
        sys.exit()

    output_filename = "seat_for_reservations_" +  input_path[-5:] 
    output_path = "output/" + output_filename
    output_file = open(output_path, "w")

    theater = Theater(10, 20, 3, 1) # (rows, seats, bufer_seats, bufer_row)
    with input_file, output_file:
        lines = input_file.readlines()
        for line in lines:
            reservation = line.split()
            res_id = reservation[0]
            res_id_pattern = re.compile(r'R\d{3}')
            if not res_id_pattern.match(res_id):
                output_file.write(res_id + ": Invalid reservation identifier\n")
                continue
            
            if not reservation[1].isdigit():
                output_file.write(res_id + ": The number of seats requested should be a positive integer\n")
                continue                

            seats_requested = int(reservation[1])
            if seats_requested > theater.seats_per_row or seats_requested < 1:
                output_file.write(res_id + ": The number of seats requested should be in range between 1 and 20\n")
                continue
            output_file.write(res_id + ": " + theater.allocate_seat(seats_requested))

            if line != lines[-1]:
                output_file.write("\n")
        output_file.close()

    print(output_path)
    return output_path


if __name__=="__main__":
    main()

