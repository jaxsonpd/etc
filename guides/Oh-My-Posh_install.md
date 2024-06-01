# Installation of Oh My Posh terminal

**Windows**:
```
winget install JanDeDobbeleer.OhMyPosh -s winget
```

Make sure $PROFILE has been created can use:
```
New-Item -Path $PROFILE -Type File -Force
```
to create a new $PROFILE file.


then add new prompt to $PROFILE using:
```
& ([ScriptBlock]::Create((oh-my-posh init pwsh --config "https://raw.githubusercontent.com/jaxsonpd/etc/main/Configs/.huvix_JD.omp.json" --print) -join "`n"))
```

then reload the profile using: 
```
. $PROFILE
```

**Unix**: 
To install simply run: 

```bash 
sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
sudo chmod +x /usr/local/bin/oh-my-posh
```

Add a new theme to the prompt by adding the following to .bashrc: 
```bash 
eval "$(oh-my-posh init bash --config "https://raw.githubusercontent.com/jaxsonpd/etc/main/Configs/.huvix_JD.omp.json")"
```

reload the profile using:
```bash
exec bash
```


Install a font with 
```
oh-my-posh font install
```



