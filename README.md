# PPT Generator
A local LLM assisted ppt generation tool 

## Why  
Writing presentations for course assignments is just boilerplate work most often, especially when even the lecturers dont even care about it.
Thats why I automated the boilerplate work, just enter a topic and the tool generates a simple presentation , enough to satisfy the base course requirement.

## Running Locally
install [ollama](https://ollama.ai/download)
and have it up and running with command `ollama serve` ( applicable to some systems only )  

download the required model ( this can be changed in this [line](https://github.com/Govind-S-B/ppt_generator/blob/main/ppt_data_gen.py#L24) )
```
ollama pull dolphin2.1-mistral
```


clone the repo and move into the directory
```
git clone https://github.com/Govind-S-B/ppt_generator.git
cd ppt_generator
```
install the required python dependencies
```
pip install -r requirements.txt
```
run the streamlit app
```
streamlit run main.py
```
