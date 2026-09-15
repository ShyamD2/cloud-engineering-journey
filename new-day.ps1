param (
    [string]$Date = (Get-Date -Format 'yyyy-MM-dd')
)

$target = Join-Path "daily-log" "$Date.md"

if (Test-Path $target) {
    Write-Warning "File already exists: $target"
} else {
    $template = Get-Content "daily-log\_template.md" -Raw
    $logContent = $template -replace "YYYY-MM-DD", $Date
    Set-Content -Path $target -Value $logContent -Encoding utf8
    Write-Host "Created new daily log: $target" -ForegroundColor Green
}
