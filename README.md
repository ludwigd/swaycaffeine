# swaycaffeine

Easy access to Sway's idle inhibitors

## Installation

The script depends on the following packages:

- python3
- python3-i3ipc

### Fedora

For Fedora there is a COPR you can use:

```
# dnf copr enable ludwigd/sway-supplemental
# dnf install swaycaffeine
```

### Other

Copy `swaycaffeine` to a location in your `$PATH`, e.g., `~/bin`, and make it executable with `chmod +x swaycaffeine`.

## Usage

Add this to your Sway config:

```
# Toggle the 'visible' inhibitor on the focused window
bindsym $mod+i exec swaycaffeine -t -i visible

# Remove inhibitors from ALL windows at once
bindsym $mod+Shift+i exec swaycaffeine --clear-all
```

For a complete list of available options, run `swaycaffeine --help`.