function getIP {
    (Get-NetIPaddress).IPv4Address | Select-String "192*"
}
function getUser{
    $env:USERNAME
}
function getHost{
    hostname
}
function getVersion{
    $host.Version.Major
}
function getDate{
    Get-Date -DisplayHint Date
}

$IP = getIP
$USER = getUser
$HOSTNAME = getHost
$VERSION = getVersion
$DATE = getDate
$BODY = "This machine's IP is $IP." + " The user is $USER." +" Hostname is $HOSTNAME." +" PowerShell Version $VERSION." +" Today's Date is $DATE"

##$BODY = This machine's IP is ...., user is $User, Hostname, PowerShell version, today's date
Send-MailMessage -To "svintsjr@mail.uc.edu" -From "svintsjr@mail.uc.edu" -Subject "IT3038 Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)