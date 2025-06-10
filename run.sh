./build.sh
sudo rm Traces/Performances-total.txt
sudo rm Traces/Performances-Continuous.txt
sudo chmod 777 traces.txt
sudo chmod 777 ./Traces
sudo chmod 777 ./Traces/*
sudo chmod 777 ./results
sudo chmod 777 ./results/*
sudo ../../build/scratch/b4mesh/./ns3.44-main-default  "$@" > traces.txt
cd scripts
sudo ./creategraphs 12
cd ..
#xdg-open results
#xdg-open traces.txt
#xdg-open ../../build/scratch/b4mesh/Traces
