 for test in $(seq 0 1 1000000); do
curl http://0.0.0.0:7007/rel &
done 