sudo  chmod a+r  ./homeassistant/.storage/**

# Add all files to the repository with respect to .gitignore rules
git add .

# Commit changes with message with current date stamp
git commit -m "automated push on `date +'%d-%m-%Y %H:%M:%S'`"

# Push changes towards GitHub
git push -u origin adtf