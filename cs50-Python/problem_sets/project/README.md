# FOCUS50
#### Video Demo:  https://www.youtube.com/watch?v=6DKLFh61Kn0
#### Description:
FOCUS50 is a command-line interface for interacting with the CS50 course content. It provides a menu for users to choose which week of the course they want to access and performs various operations such as checking performance statistics or opening a web page related to the course content.

## Files

1. `project.py`: The main script that users interact with.
2. `week.py`: Defines a `Week` class that represents a week in the CS50 course.
3. `webops.py`: Contains functions for opening a web page and handling time-related data.
4. `time_stats.py`: Contains a function for analyzing performance data related to the weeks of the course.
5. `info_x.csv`: A CSV file that contains information about the availability of different components of the CS50 course for each week.

## Usage

Run the `project.py` script in your terminal and follow the prompts.

No Arguments: If you run the script without any arguments, it will display a menu with the weeks of the course and other commands. You can choose a week by entering its number.

Week Check: If you run the script with a week number as an argument (e.g., python project.py 2), it will check the availability of different components for that week and return a link to the course content for that week.

Execute: If you run the script with two arguments, where the first one is a mode (e.g., “weeks”, “sections”, “problems”, “labs”, “psets”, “seminars”, “project”) and the second one is a week number (e.g., python project.py weeks 2), it will return a link to the specified component of the course content for that week.

Stat: If you run the script with “stat” as an argument (e.g., python project.py stat), it will check performance statistics related to the weeks of the course.

## Dependencies

This project requires Python 3.8 or later.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

