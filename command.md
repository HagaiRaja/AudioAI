# Relevant Command

##### Render form.ui

```
pyside6-uic form.ui -o ui_form.py
pyside6-rcc resource.qrc -o resource_rc.py
```

##### WhisperX function

whisperx "sounds/Jokowi Mata Najwa.mp3" --diarize --compute_type int8 --hf_token

whisperx "sounds/Vivek Podcast.mp3" --diarize --language en --compute_type int8 --hf_token
