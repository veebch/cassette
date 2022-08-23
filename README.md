
[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# Cassette

A barely-adjusted version of https://github.com/veebch/doomed that runs on a Raspberry Pi Zero and shows a YouTube subscriber number on a 128 x 128 OLED screen (**SSD1351**). A bit niche, but really easy to remix it to show some numbers you care about.

# Installation

  ```
  git clone https://github.com/veebch/cassette
  cd cassette
  cp config_example.yaml config.yaml
  ```
  
  Now you need to set up a YouTube API key that will allow you to use their API and pull your subsciption count. That key needs to be placed in the `config.yaml` file.
  
  # Wiring
| OLED  | [GPIO](https://gpiozero.readthedocs.io/en/stable/_images/pin_layout.svg) | pin no. |
|-----------|------|----|
| VCC | 3.3V | 1  |
| GND | GND | 6  |  
| MOSI/ DIN | 10 | 19 |
| CLK | 23 | 23 |
| CS  | 8 | 24 |
| DC | 24 | 18 |
| RST | 25 | 22 |

# Running

```
python3 main.py
```


