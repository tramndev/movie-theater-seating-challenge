**MOVIE THEATER SEATING CHALLENGE**

The program is managed to assign seats within a movie theater to fulfill reservation requests.

**Assumption**

The movie theater has the seating arrangement of 10 rows x 20 seats.

Seating preferences for public safety:
- A buffer of three seats and/or one row between one group and other parties is required

Seating preferences for customer satisfaction:
- All customers in the same reservation prefer to sit together in the same row. If there are more people in the reservation than available seats in a show, customers would prefer to leave for a different show than fulfill all the leftover seats or to be seated at different rows.
- Customers prefer prioritize seats that are about two thirds of the way back, as close to the center as possible for the best sound and picture.
- Otherwise, fan out to other areas by grabbing a center seat and then move forward toward the screen, rather than back toward the projector. This will let the screen fill their peripheral vision better by increasing their horizontal viewing angle.

Program settings:
- The program is managed to run one input file at a time. The program print out error message and terminate if it is provided an invalid path to input file, or wrong number of arguments.
- The input file should be a .txt file, which contains one line of input for each reservation request. (Refer to input/reservations\_2.txt for an valid example)
- Output files would be created in the folder &quot;output&quot; inside the repository.
- Invalid reservation requests would be listed in the corresponding output file along with its reservation identifier.

**Instructions**
1. Open command prompt and clone the repository using the HTTPS command: "git clone https://github.com/tramndev/movie-theater-seating-challenge.git"
2. In the directory, run the command "python process_reservation.py <input_path>" where <input_path> is the complete path to the input file. For example, we have &quot; python process\_reservation.py input/reservations\_1.txt&quot; 
3. The program will return the full path to the output file in which we can find the seat assignments and error messages if there are any invalid reservations provided.

**Resources for seating order**
- [https://www.popsci.com/find-best-seat-movie-theater/](https://www.popsci.com/find-best-seat-movie-theater/)
- [https://www.groupon.com/articles/best-movie-theater-seats](https://www.groupon.com/articles/best-movie-theater-seats)