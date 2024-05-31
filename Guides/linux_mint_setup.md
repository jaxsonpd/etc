# Linux Mint Install

This guide dictates my linux mint install process including the key packages and bug fixes

# Install
Install from linux mint. Ensuring:
- Secure Boot Enabled
- BitLocker is off (if dual booting)
- EUFI bios enabled
- Windows fast boot disabled (if dual booting)
- Disable TPM (and hide it)

# Fix Nvidias BS
Sometimes Nvidia drivers dont place nice with windows dual boot or linux in general so best to make sure they are downloaded correctly the way to do this is to run:

```
sudo apt-get purge nvidia*
```

Then run:
```
sudo apt autoremove
sudo ubuntu-drivers autoinstall
```

# Fix Casper
If boot problems occur then remove this to help remove some of the erros.
```bash
sudo apt remove --purge casper
```

# Key Installs
- neovim
- oh my posh
- gh cli
- chrome
- latex

# Latex Install
First get texlive using:

```
sudo apt install texlive-latex-base
```

Then install apt-file to search for packages:

```
sudo apt-get install apt-file
sudo apt-file update
```
Then packages can be searched for using:

```
apt-file search /package.sty
```

Packages I need are:

- texlive-latex-recommended
- texlive-bibtex-extra
- texlive-latex-extra
- biber
