ARRAY_SIZE=1
TIME_PER_LOOP=5
LOOP=27
for i in $(seq 1 $LOOP)
do
	gcc -DSTREAM_ARRAY_SIZE=$ARRAY_SIZE -mtune=native -march=native -fopenmp -mcmodel=small -DNTIME=$TIME_PER_LOOP -o ./stream/stream ./stream/stream.c
	./stream/stream > stream-res-$1-$2-$i
	rm ./stream/stream
	ARRAY_SIZE=$(($ARRAY_SIZE*2))
done