# ALFRED

ALFRED V1 (Python 3 advanced Outlook automation Tool)

**OBJECTIVE:**

    ALFRED is a virtual assistant for quick email automation.

    ALFRED aims to provide a quick and easy RPA capability for EMAIL base organizations where multiple tasks
    could be automated but still depend on a person "processing" such tasks.

    Therefore this RPA is a engine for WORKFORCE and WORKFLOW optimization, taking care of the repetitive tasks
    such as generating and emailing reports, forward emails to the same people, classifing emails, etc.

**Working Features:**

    - Email core class defined based on OUTLOOK specification.
    - Load Outlook emails from main Inbox
    - Run multiple regex analysis on strings (Such as Email: Subject / Body)

**Log:**

    - 19/4:
        - Setup .VENV for better development.
        - ADD multiple exceptions to .gitignore
        - ADD settings.py for main config.

    - 17/4 first package build. readEmails + regularExpressions have been connected. Since this is the very core of this system.
