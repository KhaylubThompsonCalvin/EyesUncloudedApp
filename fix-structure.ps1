# ==============================================================================
# File: fix-structure.ps1
# Author: Khaylub Thompson-Calvin
# Description:
# Reorganizes Eyes Unclouded App project structure and ensures template scaffolding.
# ==============================================================================

Write-Output "Starting project structure reorganization..."

# Step 1: Move clarifying questions (if exists)
if (Test-Path ".\clarifying-questions.md") {
    Move-Item ".\clarifying-questions.md" "docs\notes\" -Force
    Write-Output "Moved clarifying-questions.md to docs/notes/"
} elseif (Test-Path ".\clarifying-questions.txt") {
    Move-Item ".\clarifying-questions.txt" "docs\notes\" -Force
    Write-Output "Moved clarifying-questions.txt to docs/notes/"
} else {
    Write-Output "No clarifying questions file found."
}

# Step 2: Move implementation notes
if (Test-Path ".\implementation-notes.md") {
    Move-Item ".\implementation-notes.md" "docs\notes\" -Force
    Write-Output "Moved implementation-notes.md to docs/notes/"
} else {
    Write-Output "No implementation-notes.md file found."
}

# Step 3: Move system flow diagram
if (Test-Path ".\system_flow_diagram.txt") {
    Move-Item ".\system_flow_diagram.txt" "docs\diagrams\" -Force
    Write-Output "Moved system_flow_diagram.txt to docs/diagrams/"
}

# Step 4: Ensure HTML templates exist
function Ensure-TemplateExists($filename, $content) {
    $path = "src\views\templates\$filename"
    if (-not (Test-Path $path)) {
        $content | Out-File -FilePath $path -Encoding UTF8
        Write-Output "Created placeholder: $filename"
    } else {
        Write-Output "$filename already exists"
    }
}

Ensure-TemplateExists "login.html" @"
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h1>Login</h1>
    <form action='/login' method='post'>
        <label>Username or Email:</label><input type='text' name='username' />
        <label>Password:</label><input type='password' name='password' />
        <button type='submit'>Login</button>
    </form>
</body>
</html>
"@

Ensure-TemplateExists "register.html" @"
<!DOCTYPE html>
<html>
<head><title>Register</title></head>
<body>
    <h1>Register</h1>
    <form action='/register' method='post'>
        <label>Full Name:</label><input type='text' name='fullname' />
        <label>Username:</label><input type='text' name='username' />
        <label>Email:</label><input type='email' name='email' />
        <label>Password:</label><input type='password' name='password' />
        <label>Confirm Password:</label><input type='password' name='confirmPassword' />
        <button type='submit'>Register</button>
    </form>
</body>
</html>
"@

Ensure-TemplateExists "dashboard.html" @"
<!DOCTYPE html>
<html>
<head><title>Dashboard</title></head>
<body>
    <h1>Dashboard</h1>
    <p>Welcome to the Dashboard. Notifications will appear here.</p>
</body>
</html>
"@

Write-Output "✅ Project structure reorganization complete."

