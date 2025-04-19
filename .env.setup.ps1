Write-Host "?? Eyes Unclouded – Secure .env Setup" -ForegroundColor Cyan

$secretKey = Read-Host "Enter your SECRET_KEY"
$mongoUri  = Read-Host "Enter your MONGO_URI"

@"
SECRET_KEY=$secretKey
MONGO_URI=$mongoUri
"@ | Set-Content .env

Write-Host "`n? .env file has been created successfully." -ForegroundColor Green
