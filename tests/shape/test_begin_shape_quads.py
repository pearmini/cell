import lighght as gh

# environment
gh.full_screen()
gh.no_cursor()

# styles
gh.fill('*', gh.YELLOW, gh.RED)
gh.stroke('@', gh.GREEN, gh.BLUE)

# custom shapes
gh.begin_shape(gh.QUADS)
gh.vertex(1, 1)
gh.vertex(1, 6)
gh.vertex(6, 6)
gh.vertex(6, 1)
gh.vertex(11, 1)
gh.vertex(11, 6)
gh.vertex(16, 6)
gh.vertex(16, 1)
gh.end_shape(close_mode=gh.CLOSE)

gh.run()