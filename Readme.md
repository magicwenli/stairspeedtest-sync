# Test and filter your v2ray subscription

Keep your subscription alive.

## Usage

Configure your `config.json`, then type

```bash
docker run -it --name stairspeedtest -v `pwd`:/root/workdir multiarch/alpine:amd64-latest-stable  /bin/sh -c "cd /root/workdir && sh scripts/speedtest.sh"
```

This should download latest stairspeedtest_reborn_linux64 from [magicwenli/stairspeedtest-reborn/releases](https://github.com/magicwenli/stairspeedtest-reborn/releases), and run stairspeedtest.

After that, a subscription file `public/v2sync/subscripts.txt`(default path) will be generated.

Use Nginx or other file server to expose it.

Add a crontab may be helpful. 

```crontab
0 7,19 * * * docker start stairspeedtest >/dev/null 2>&1
```


## Credits

- [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn)

- [ShiroNekoWorks/v2sync](https://github.com/ShiroNekoWorks/v2sync)