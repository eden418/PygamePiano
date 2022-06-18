\version "2.22.2"
upper = {
\clef treble
 ges'  c'  des'  d'  ees'  e' 
}
lower = {
\clef bass c des d ees c des d ees e
}
\score {
\new PianoStaff
<<\new Staff = "upper" \upper
\new Staff = "lower" \lower>>
}