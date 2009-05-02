# Twitter Publisher

This is just a sample project using twitty-twister and wokkel to
publish a twitter realtime stream (e.g. spritzer, gardenhose or
firehose) via xmpp pubsub.

It doesn't reconnect the HTTP stream on failure, but that's primarily
because I don't keep it running long enough to do so.  Anyone who
cares can add that minor feature.  :)

# How Do I Do It?

    git clone git://github.com/dustin/twitter-pub.git
    cd twitter-pub
    git submodule init
    git submodule update
    cp pub.tac.in pub.tac

Edit pub.tac to suit your needs (your xmpp service, twitter account,
etc...).  Start it up (`-n` for foreground):

    twistd -ny pub.tac
