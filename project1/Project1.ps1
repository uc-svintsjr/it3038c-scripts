#Name: Joseph Svintsitsky
#Module: Project 1
#Due Date: 10/3/2021
#Assignment: Write a PowerShell script that uses the speech synthesizer
#Goal: The goal of this script is to have Microsoft David & Zira sing a love duet of "Ain't No Mountain High Enough" by Marvin Gaye
#How to Run: Simply press "Run Script" (f5) and the song will begin. Enjoy!
#Resources: https://mikerodrick.com/2020/07/09/windows-powershell-text-to-speech/

# Defining a assembly path because the SpeechSynthesizer class is only on the .NET framework
$assemblyPath = 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\WPF\System.Speech.dll'

# Adding assembly dynamic link library (dll) for the pupose of targeting the .NET framework libraries
Add-Type -Path $assemblyPath

# Create new objects so that they can be called and sing the song
$david = New-Object System.Speech.Synthesis.SpeechSynthesizer
$zira = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Change voice to Zira so we can incorporate a female voice
$zira.SelectVoice('Microsoft Zira Desktop')

# Default speed was to slow, so it needed to be sped up
$david.Rate = 3
$zira.Rate = 3

# [Ain't No Mountain High Enough by Marvin Gaye]

# Verse 1: Marvin Gaye
$david.Speak("Listen, baby")
$david.Speak("Ain't no mountain high")
$david.Speak("Ain't no valley low")
$david.Speak("Ain't no river wide enough, baby")

# Tammi Terrell
$zira.Speak("If you need me, call me")
$zira.Speak("No matter where you are")
$zira.Speak("No matter how far (Don't worry, baby)")
$zira.Speak("Just call my name")
$zira.Speak("I'll be there in a hurry")
$zira.Speak("You don't have to worry")
$zira.Speak("Cause baby there")

# Out-Null hides the output instead of sending it down the pipeline or displaying it.
# Chorus: Marvin Gaye & Tammi Terrell 
$david.speakasync("Ain't no mountain high enough") | Out-Null
$zira.speakasync("Ain't no mountain high enough") | Out-Null
$david.speakasync("Ain't no valley low enough") | Out-Null
$zira.speakasync("Ain't no valley low enough") | Out-Null
$david.speakasync("Ain't no river wide enough") | Out-Null
$zira.speakasync("Ain't no river wide enough") | Out-Null
$david.speakasync("To keep me from getting to you, babe") | Out-Null
$zira.speakasync("To keep me from getting to you, babe") | Out-Null

# Verse 2: Marvin Gaye

$david.Speak("Remember the day")
$david.Speak("I set you free")
$david.Speak("I told you you could always count on me, darling")
$david.Speak("From that day on, I made a vow")
$david.Speak("I'll be there when you want me")
$david.Speak("Someway, somehow")
$david.Speak("Oh baby there")

#Chorus: Marvin Gaye & Tammi Terrell 
$david.speakasync("Ain't no mountain high enough") | Out-Null
$zira.speakasync("Ain't no mountain high enough") | Out-Null
$david.speakasync("Ain't no valley low enough") | Out-Null
$zira.speakasync("Ain't no valley low enough") | Out-Null
$david.speakasync("Ain't no river wide enough") | Out-Null
$zira.speakasync("Ain't no river wide enough") | Out-Null
$david.speakasync("To keep me from getting to you, babe") | Out-Null
$zira.speakasync("To keep me from getting to you, babe") | Out-Null

# Bridge: Marvin Gaye
$david.Speak("Oh no, darling")

# Tammi Terrell
$zira.Speak("No wind, no rain")
$zira.Speak("Nor winter storm")
$zira.Speak("Can't stop me, baby")

# Marvin Gaye
$david.Speak("No, no baby")

# Tammi Terrell
$zira.Speak("Cause you are my goal")

# Marvin Gaye
$david.Speak("If you're ever in trouble")
$david.Speak("I'll be there on the double")
$david.Speak("Just send for me")

# Marvin Gay & Tammi Terrell
$david.speakasync("Oh, baby!") | Out-Null
$zira.speakasync("Oh, baby!") | Out-Null

# Verse 3
$david.speakasync("My love is alive") | Out-Null
$zira.speakasync("My love is alive") | Out-Null
$david.speakasync("Way down in my heart") | Out-Null
$zira.speakasync("Way down in my heart") | Out-Null
$david.speakasync("Although we are miles apart") | Out-Null
$zira.speakasync("Although we are miles apart") | Out-Null

# Marvin Gaye
$david.Speak("If you ever need a helping hand")
$david.Speak("I'll be there on the double")
$david.Speak("Just as fast as I can")

#Chorus: Marvin Gaye & Tammi Terrell 
$david.speakasync("Don't you know that there...") | Out-Null
$zira.speakasync("Don't you know that there...") | Out-Null
$david.speakasync("Ain't no mountain high enough") | Out-Null
$zira.speakasync("Ain't no mountain high enough") | Out-Null
$david.speakasync("Ain't no valley low enough") | Out-Null
$zira.speakasync("Ain't no valley low enough") | Out-Null
$david.speakasync("Ain't no river wide enough") | Out-Null
$zira.speakasync("Ain't no river wide enough") | Out-Null
$david.speakasync("To keep me from getting to you, babe") | Out-Null
$zira.speakasync("To keep me from getting to you, babe") | Out-Null
$david.speakasync("Ain't no mountain high enough") | Out-Null
$zira.speakasync("Ain't no mountain high enough") | Out-Null
$david.speakasync("Ain't no valley low enough") | Out-Null
$zira.speakasync("Ain't no valley low enough") | Out-Null
$david.speakasync("Ain't no river wide enough") | Out-Null
$zira.speakasync("Ain't no river wide enough") | Out-Null
$david.speakasync("Ain't no mountain high enough") | Out-Null
$zira.speakasync("Ain't no mountain high enough") | Out-Null
$david.speakasync("Ain't no valley low enough") | Out-Null
$zira.speakasync("Ain't no valley low enough") | Out-Null