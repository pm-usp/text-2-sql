echo "GENERATING RESULTS INFORMATION - EM - Structure Indicator"

python main.py \
--execution result_analysis \
--perspective process_mining \
--metric EM

python main.py \
--execution result_analysis \
--perspective nlp \
--metric EM

python main.py \
--execution result_analysis \
--perspective sql \
--metric EM

echo "GENERATING RESULTS INFORMATION - EX - Run Indicator"

python main.py \
--execution result_analysis \
--perspective process_mining \
--metric EX

python main.py \
--execution result_analysis \
--perspective nlp \
--metric EX

python main.py \
--execution result_analysis \
--perspective sql \
--metric EX