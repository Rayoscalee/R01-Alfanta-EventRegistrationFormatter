Student Event Registration Formatter

Description
This program formats student event registration details.

Language Used
Python

String Feature Used
`strip()`, `title()`, `upper()`

Date/Time Feature Used
`datetime` (`strftime()`)

Version History
- Version 1: Basic input and output
- Version 2: Added string formatting
- Version 3: Added date formatting

Sample Output
```text
Enter student first name: juan
Enter student last name: dela cruz
Enter section: magnesium
Enter event name: science fair
Enter event year: 2026
Enter event month: 6
Enter event day: 3

Student Event Registration Summary
Name: Juan Dela Cruz
Name Code: JUAN DELA CRUZ
Section: MAGNESIUM
Event: Science Fair
Event Date: June 3, 2026
Language Used: Python
String Feature Used: strip(), title(), upper()
Date/Time Feature Used: datetime
Registration record created successfully.
```

Reflection
 Student Event Registration Formatter

 Description
This program formats student event registration details.

 Language Used
Python

 String Feature Used
`strip()`, `title()`, `upper()`

 Date/Time Feature Used
`datetime` (`strftime()`)

 Version History
Version 1: Basic input and output
Version 2: Added string formatting
Version 3: Added date formatting


 Reflection
In my first version, my program could only take inputs from the user and print them back out as they were typed, even if 
the capitalization was messy. I improved my program by updating it step by step in gitHub to automatically clean the text 
and format the event date. The string methods I used were `strip()`, `title()`, and `upper()` because they remove accidental spaces 
and keep names, sections, and event titles uniform. The date/time feature I used was `datetime` with `strftime()` because it turns 
plain numbers like `6` and `3` into a clean, readable date like `June 3, 2026`. The biggest change in my program was making 
the final summary look neat and reliable no matter how carelessly a student types their details.
