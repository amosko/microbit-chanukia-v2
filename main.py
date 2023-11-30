def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(2000)
    pins.digital_write_pin(DigitalPin.P8, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P9, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.set_tempo(120)
    for index in range(2):
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(220, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
    for index2 in range(2):
        music.play(music.tone_playable(220, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(330, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.set_tempo(120)
    for index3 in range(2):
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 1)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P1, 1)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P2, 1)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P8, 1)
        music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P9, 0)
        music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P9, 0)
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P8, 0)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P2, 0)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P1, 0)
        music.play(music.tone_playable(330, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P9, 0)
        music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(220, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
    for index4 in range(2):
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(220, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P9, 0)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P3, 1)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P3, 0)
        pins.digital_write_pin(DigitalPin.P8, 1)
        music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P8, 1)
        music.play(music.tone_playable(440, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        pins.digital_write_pin(DigitalPin.P9, 1)
        music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P2, 0)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P3, 1)
        music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        pins.digital_write_pin(DigitalPin.P3, 0)
        pins.digital_write_pin(DigitalPin.P1, 1)
        music.play(music.tone_playable(330, music.beat(BeatFraction.BREVE)),
            music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(349, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(330, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(294, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(247, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(220, music.beat(BeatFraction.BREVE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

pins.digital_write_pin(DigitalPin.P0, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P1, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P2, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P8, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 1)
basic.pause(2000)
pins.digital_write_pin(DigitalPin.P8, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P2, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P1, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P0, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 0)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 1)
basic.pause(100)
pins.digital_write_pin(DigitalPin.P9, 0)