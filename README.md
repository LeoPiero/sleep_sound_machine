sleep_sound_machine
Requires GNU/Linux SoX, "play" command to work.
Utilizes play command to generate noise.
Use cron (or similar) to schedule the noise to play just before sleeping hours.
Quiet time starts at 7:00AM which is when the program will terminate.

Plays noise to help drown out ambient sounds. Default "quiet time" from 7:00AM until 9:30PM.
You can customize the quiet time by modifying the morning_time and evening_time variables.
