enum SYS_IO_ReceiverStatusBit {
    READY,
    BUSY,
    OFFLINE
};

int main() {
    enum SYS_IO_ReceiverStatusBit status = BUSY;
    status = READY;
}
