# Installation of Oh My Posh terminal

**Windows**:
```
winget install JanDeDobbeleer.OhMyPosh -s winget
````

Make sure $PROFILE has been created can use:
```
New-Item -Path $PROFILE -Type File -Force
```
to create a new $PROFILE file.


then add new prompt to $PROFILE using:
```
& ([ScriptBlock]::Create((oh-my-posh init pwsh --config "$env:POSH_THEMES_PATH\huvix.omp.json" --print) -join "`n"))
```

then reload the profile using: 
```
. $PROFILE
```

**Unix**:
```
brew install jandedobbeleer/oh-my-posh/oh-my-posh
```
if homebrew is not installed run:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
and remember to add to path.

Add a new theme to the prompt using:

```
eval "$(oh-my-posh init zsh --config $(brew --prefix oh-my-posh)/themes/huvix.omp.json)"
```

reload the profile using:
```
exec bash
```


Install a font with 
```
oh-my-posh font install
```



