
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ProjectRoot


if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "`n[ERRO] Python não está instalado ou não está no PATH." -ForegroundColor Red
    exit
}

if (-not (Test-Path "$ProjectRoot\venv")) {
    Write-Host "`n[+] Criando ambiente virtual..."
    python -m venv venv
} else {
    Write-Host "`n[+] Ambiente virtual já existe. Pulando criação..."
}

Write-Host "`n[+] Ativando ambiente virtual..."
& "$ProjectRoot\venv\Scripts\Activate.ps1"


if (Test-Path "$ProjectRoot\requirements.txt") {
    Write-Host "`n[+] Instalando dependências..."
    pip install --upgrade pip
    pip install -r requirements.txt
} else {
    Write-Host "`n[!] requirements.txt não encontrado. Pulando instalação de dependências." -ForegroundColor Yellow
}


Write-Host "`n[✓] Iniciando o jogo..."
pgzrun app.py
