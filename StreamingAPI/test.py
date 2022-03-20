import twint

# Configure
c = twint.Config()
c.Search = "#resbakuna OR #bidabakunation OR #moderna OR #modernavaccine"
c.Lang = "tl"
c.Since = "2021-12-1"
c.Until = "2022-1-18"
c.Store_csv = True
c.Output = "test.csv"

# Run
twint.run.Search(c)