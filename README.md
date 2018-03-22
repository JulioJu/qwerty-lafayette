One Dead Key To Rule Them All

# Nobody Likes Dead Keys

Many languages use several types of diacritics. Supporting them with the standard `qwerty-intl` layout is often possible but requires one dead key per diacritic: `'` is a dead acute, `"` is a dead diaeresis, `^` is a dead circumflex, etc. This raises two issues:

- these dead keys can be quite far to reach, making it uncomfortable to write a text in a non-English language;
- they get in the way when coding or writing in English, e.g. typing a double quote sign requires two key presses (`"` + space).

As a result, nobody likes dead keys. The `qwerty-intl-nodeadkeys` is a popular variant among developers but it makes it even more uncomfortable to type a non-English text.

# One Dead Key (1dk) To Rule Them All

The idea is to use a single dead key (called `1dk`) for all diacritical characters, the behavior of this unique dead key being specific to every language.

## Main Role

The `1dk` acts as a dead diacritic, which is chosen according to the current locale (language).

E.g. for Spanish, the main role is the acute accent and can be applied on all vowels:

- `1dk` + `a` = `á`
- `1dk` + `e` = `é`
- `1dk` + `i` = `í`
- `1dk` + `o` = `ó`
- `1dk` + `u` = `ú`

Whereas for Italian, the main role would be the grave accent:

- `1dk` + `a` = `à`
- `1dk` + `e` = `è`
- `1dk` + `i` = `ì`
- `1dk` + `o` = `ò`
- `1dk` + `u` = `ù`

Beside this main role, the `1dk` can have an extended behavior on some other keys. E.g. in Spanish:

- `1dk` + `n` = `ñ`
- `1dk` + `!` = `¡`
- `1dk` + `?` = `¿`

The main role should cover the most frequent special characters for a given language, while remaining intuitive.

## Secondary Roles

Most European languages use more than one diacritic. Rather than using several dead keys on the same letter, the idea here is to use the same dead key on several letters.

As an example, for French and Italian the `e` can have a grave (`è`) or an acute (`é`) accent, and it is the only letter that can have an acute accent — so dedicating a dead acute key would be a pity. Instead, the `1dk` can be used like this on qwerty keyboards:

- `1dk` + `w` = `é`
- `1dk` + `e` = `è`

This is a trade-off between intuitiveness and efficiency. Keeping a consistent logic for these secondary roles makes it easier to use.

For qwerty and dvorak keyboards, the following rules can be a good way to support two more diacritics on vowels:

- `1dk` + (key below a vowel) = a second diacritic (e.g. grave for Spanish)
- `1dk` + (key above a vowel) = a third diacritic

<!-- And of course, another dead diacritic can still be added to `shift`+`1dk`. -->

## Punctuation & Symbols

The `1dk` can also be used on non-letters to get more punctuation signs and symbols, e.g.:

- `1dk` + `.` = `…` (ellipsis)
- `1dk` + `-` = `—` (mdash)
- `1dk` + `$` = `¢`
- `1dk` + `%` = `‰`
- `1dk` + `0` = `°`

It is also commonly used to support language-specific quote signs, though not intuitively. The following is an easy way to add English (`“”`) and German (`„“`) quote signs:

- `1dk` + `1` = `„`
- `1dk` + `2` = `“`
- `1dk` + `3` = `”`

## Pros & Cons

Compared to the usual `qwerty-intl` approach (= one dead key per diacritic), the `1dk` approach brings the following benefits:

- better efficiency & comfort: much less finger movement
- fewer dead keys get in the way when coding or writing in English
- supports more language-specific characters (e.g. quote signs, symbols…)
- supports non-Latin languages, e.g. Polish, Czech, Turkish, Esperanto…

The main drawback is that it is less intuitive. Expect a steeper learning curve than with `qwerty-intl`.

# Which Key Should Be The `1dk`?

On a standard US-qwerty keyboard, the most intuitive keys are:

- the quote sign (`'`), for users who want the `1dk` to be easy to reach;
- or the back tick (````), for users who want to make sure that no dead key will get in the way while typing code or in English.

With a US-Dvorak layout, the quote key (`'`) is a possible choice but not the easiest key to chain with vowels. The dash key (`-`) chains nicely and is easy to reach, which makes it a better choice.

Fearless users can also consider tweaking their own layout to make the `1dk` a dedicated key on their keyboard, so that it’s even easier to reach without sacrificing a common key such as the quote sign — see the [qwerty42](http://qwerty-lafayette.org/) project for instance.

# Technical Considerations

## Windows

The 1dk toolchain produces a `*.klc` file (warning: encoded in utf16-LE). You’ll need the MS Keyboard Layout Creator to turn this `*.klc` file into a layout installer.

## MacOSX

The 1dk toolchain produces a `*.keylayout` file.

Known issue: X11 apps will use the `1dk` as a classical dead diacritic. You can use an `~/.XCompose` file to re-define the full behavior of your `1dk`.

## GNU/Linux

The 1dk toolchain produces an `*.xkb` file. 

