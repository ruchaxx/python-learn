FROM alpine:latest
RUN echo "tmp file" > /tmp/tmp.txt
RUN mkdir /tmp/abc
RUN echo "tmp1 file" > /tmp/abc/tmp1.txt
CMD ["sh", "-c", "while true; do sleep 1; done"]