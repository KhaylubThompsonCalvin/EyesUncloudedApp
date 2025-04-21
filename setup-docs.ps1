# ==============================================================================
# File: setup-docs.ps1
# Project: Eyes Unclouded App
# Author: Khaylub Thompson-Calvin
# Date: 04/19/2025
# Description:
# Reorganizes docs folder, archives legacy content, and prepares screenshot,
# notes, and diagram structure with new placeholders.
# ==============================================================================

Write-Output "`n--- Starting documentation setup... ---"

# Archive current docs
if (Test-Path "docs") {
    Rename-Item -Path "docs" -NewName "docs_old" -Force
    Write-Output "Archived existing docs folder to docs_old/"
}

# Recreate fresh docs structure
New-Item -ItemType Directory -Path "docs\screenshots" -Force | Out-Null
New-Item -ItemType Directory -Path "docs\notes" -Force | Out-Null
New-Item -ItemType Directory -Path "docs\diagrams" -Force | Out-Null
Write-Output "Created new docs/ structure."

# Touch diagram placeholder
New-Item -ItemType File -Path "docs\diagrams\eyes_unclouded_flow.txt" -Force | Out-Null

# Touch notes placeholder
New-Item -ItemType File -Path "docs\notes\implementation_notes_eyes_unclouded.md" -Force | Out-Null

# Screenshot documentation plan
Set-Content "docs\notes\screenshot_plan.md" @"
# Eyes Unclouded App – Screenshot Documentation Plan

## Core Screens
- splash_screen.png
- register_ui.png
- login_ui.png
- dashboard_main.png
- send_notification_ui.png
- notification_log.png
- emotion_log_ui.png
- class_reveal_page.png
- oracle_archive_upload.png
- mentor_insight_ui.png

## Optional Additions
- template_builder_ui.png
- settings_ui.png
- perception_timeline.png
- mobile_view_dashboard.png
"@

Write-Output "--- Documentation setup complete. ---"

