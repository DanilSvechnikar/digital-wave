## Init locally
1. Clone existing project
    ```bash
    git clone https://github.com/DanilSvechnikar/digital-wave.git
    cd digital-wave
    ```

2. **Create and activate a virtual environment before installing packages!!!**
<br></br>

3. Packet initialization. About +-1.5GB
    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

### Run
From the root of the project, run [predict_model.py](predict_model.py):
```bash
python predict_model.py
```

В каталоге [demo_data](data/demo_data) находятся изображения с тракторами и людьми \
Запущенный файл выполнит предсказания с помощью YOLO для всех изображений в каталоге \
Изображения с отрисованными bounding boxes будут сохранены в [Pred_images](data/Pred_images) \
Метки классов и координаты bounding boxes будут сохранены в txt файлы в [Pred_txt](data/Pred_txt)
