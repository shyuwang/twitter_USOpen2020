# twitter_USOpen2020

## Overview
The aim of this project is to study how Twitter API works and how Spark Streaming integrates with it. I use Twitter API to obtain realtime tweets during USOpen 2020 and visualize the top 20 popular users at the time.

Please see `twitter_usopen2020.md` for analysis, or get access to the analysis at [my blog](https://shyuwang.github.io/2020/09/11/twitter_usopen/).

## How to run
First run `twitter_app.py` in terminal, establishing the connection at with `localhost` `TCP_IP` and at certain `TCP_PORT`. After that, run `my_spark_streaming.ipynb` file to receive the stream tweet data and visualize with bar plot.
