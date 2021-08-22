**This project is just a wrapper for the brilliant work done in [pyHS100](https://github.com/GadgetReactor/pyHS100).**

This project provides a nice and easy way to turn off the status LEDs for Kasa smartplugs, see more on the problem here: https://www.reddit.com/r/HomeNetworking/comments/8c1fx2/how_do_you_turn_off_the_led_indicator_in_a_tplink/

"*Piece of tape*" - **this just won't do...**

**Supported devices**

* Plugs
  * HS100
  * HS103
  * HS105
  * HS110

### Requirements

```
pip install -r requirements.txt
```

# Usage

### Discovery Only

Don't provide any options to run a discovery scan for Kasa smartplugs and their LED status:

```
> python kasa-dark-mode.py
Plug Alias: Fan
Current LED state: False
---
Plug Alias: Network
Current LED state: False
---
```

### One for all

Use `-l` or `-d` to set light (LED on) or dark (LED off) mode for all discovered Kasa smartplugs:

```
> python kasa-dark-mode.py -d
Plug Alias: Fan
Current LED state: True
New LED state: False
---
Plug Alias: Network
Current LED state: True
New LED state: False
```

### Interactive mode (`-i`, `--interactive`)

Use interactive mode to toggle LED status lights for each discovered Kasa Plug:

```
> python kasa-dark-mode.py -i
You have selected interactive mode
Searching for smartplugs...
--plug found--
Plug Alias: Fan
Current LED state: False
Do you wish to turn ON 'Fan' LED [Y/n]: n
---
--plug found--
Plug Alias: Network
Current LED state: True
Do you wish to turn OFF 'Network' LED [Y/n]:
New LED state: False
---
```

