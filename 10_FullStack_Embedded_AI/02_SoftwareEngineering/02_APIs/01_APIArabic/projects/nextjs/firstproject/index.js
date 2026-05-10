const protobuf = require("protobufjs");
const sizeof = require("object-sizeof");

async function run() {
    // ✅ correct usage (static load, NOT root.load)
    const root = await protobuf.load("./resources/player.proto");

    const PlayerMessage = root.lookupType("PlayerMessage");

    const obj = {
        id: 1,
        first: `Mohamed`,
        last: `ferganey`,
        email: "ahmed.ferganey707@gmail.com",
    };

    const err = PlayerMessage.verify(obj);
    if (err) throw Error(err);

    const payload = PlayerMessage.create(obj);

    console.log(`payload size: ${sizeof(payload)} bytes`);

    const buffer = PlayerMessage.encode(payload).finish();

    console.log("serialized buffer:", buffer);
    console.log(`buffer size: ${sizeof(buffer)} bytes`);

    const decodedMessage = PlayerMessage.decode(buffer);

    const decodedObject = PlayerMessage.toObject(decodedMessage, {
        longs: String,
        enums: String,
        bytes: String,
        defaults: true
    });

    console.log("decoded object:", decodedObject);
}

run();