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

```bash
sudo apt-get purge nvidia*
```

Then run:
```bash
sudo apt autoremove
sudo ubuntu-drivers autoinstall
```

# Fix Casper
If boot problems occur then remove this to help remove some of the erros.
```bash
sudo apt remove --purge casper
```

# Fsck Repair
If boot problems persist then force linux to run a fsck repair if need at boot by following this guide: https://www.linuxuprising.com/2019/05/how-to-force-fsck-filesystem.html. 

# Key Installs
- neovim
- oh my posh
- gh cli
- chrome
- latex

# Fonts
Install fonts using the nerd font I like CaskaydiaMono. Then move it into ~/.local/share/fonts/NerdFonts/.

# Latex Install
First get texlive using:

```bash
sudo apt install texlive-latex-base
```

Then install apt-file to search for packages:

```bash
sudo apt-get install apt-file
sudo apt-file update
```
Then packages can be searched for using:

```bash
apt-file search /package.sty
```

Packages I need are:

- texlive-latex-recommended
- texlive-bibtex-extra
- texlive-latex-extra
- biber
