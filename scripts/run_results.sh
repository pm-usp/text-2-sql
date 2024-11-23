echo "GENERATING RESULTS INFORMATION - EM - Structure Indicator"

echo "PROCESS MINING"
python main.py \
--execution result_analysis \
--perspective process_mining \
--metric EM

echo "NLP STATISTICS"
python main.py \
--execution result_analysis \
--perspective nlp \
--metric EM

echo "SQL STATISTICS"
python main.py \
--execution result_analysis \
--perspective sql \
--metric EM

echo "GENERATING RESULTS INFORMATION - EX - Run Indicator"

echo "PROCESS MINING"
python main.py \
--execution result_analysis \
--perspective process_mining \
--metric EX

echo "NLP STATISTICS"
python main.py \
--execution result_analysis \
--perspective nlp \
--metric EX

echo "SQL STATISTICS"
python main.py \
--execution result_analysis \
--perspective sql \
--metric EX