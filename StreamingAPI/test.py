import twint

# Configure
c = twint.Config()
c.Search = "Ukraine war"

# Run
twint.run.Search(c)