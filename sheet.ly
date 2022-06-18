\version "2.22.2"
upper = {
\clef treble
 c'  des'  d'  ees'  e'  ges'  f'  e'  ges'  ees'  des'  aes'  bes'  f'  g'  f'  g'  aes'  aes'  bes'  a'  a'  a'  aes'  g'  g'  g'  g'  g'  g'  g'  bes'  bes'  b'  bes'  ees'  aes'  ges'  d'  f'  g'  e'  d'  f'  e'  d'  f'  g'  e'  d'  g'  f'  e'  d'  g'  f'  e'  d' 
}
lower = {
\clef bass des ees c ees des c des des des ees f ges c d e g c d e g c d e f c d e f g a b a b c d e g des ees f aes ges aes bes b bes b des ges aes a aes ges des c d d ges aes a aes ges d des des des ges aes a aes ges d b bes b a aes a aes ges des des ees f ges e g c d e g bes b g c d e g c d e g c e d g
}
\score {
\new PianoStaff
<<\new Staff = "upper" \upper
\new Staff = "lower" \lower>>
}