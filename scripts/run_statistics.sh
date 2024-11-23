echo "GENERATING DATASET STATISTICS INFORMATION AND GRAPHS"

echo "PROCESS MINING STATISTICS"
python main.py \
--execution dataset_statistics \
--perspective process_mining

echo "NLP STATISTICS"
python main.py \
--execution dataset_statistics \
--perspective nlp

echo "SQL STATISTICS"
python main.py \
--execution dataset_statistics \
--perspective sql