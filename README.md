# Table Generator
This is a simple generic content-generator written in Python, meant to model D&D style 
encounter/event tables. Content goes in a json file (e.g. 
[`heist.json`](https://gist.github.com/mammothbane/cafb7d6c9f61d824c4ce2f7fd079325b)), and the
program picks random values out of that file.

The json file is quite simple. At its most basic, it looks like this:

```json
{
  "name": "example_name",
  "parameters": {
    "example_category": [
      "example_content_1",
      "example_content_2"
    ]
  }
}
```

Supposing the file described above is `example.json`, we run the program as follows:

```bash
$ python main.py example.json
generating "example_name"
    example_category: example_content_2
```

Each key in the `parameters` object in the json file gets its own entry in the output,
with a value picked randomly. Just add more entries to the file to see more 
varied output. It's also suggested to keep different files around for different types of tables.
E.g. you might have `weather.json` to model weather events, which could look like this:

```json
{
  "name": "weather",
  "parameters": {
    "clouds": [
      "clear",
      "partly cloudy",
      "overcast"
    ],
    "precipitation": [
      "clear",
      "rain",
      "snow"
    ]
  }
}
```

as well as `npc_encounter.json`, or `vehicle_trouble.json`, or whatever else you can think of
(you could transcribe all the tables in the PHB/DMG if you want!). Then, just specify which table
you want to generate by filename.
