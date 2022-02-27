# Test and filter your v2ray subscribes

## Usage

Configure your `config.json`, then type

```bash
docker run -it --name stairspeedtest -v `pwd`:/root/workdir multiarch/alpine:amd64-latest-stable  /bin/sh -c "cd /root/workdir && sh scripts/speedtest.sh"
```

This should download latest stairspeedtest_reborn_linux32 from [magicwenli/stairspeedtest-reborn/releases](https://github.com/magicwenli/stairspeedtest-reborn/releases), and run speedtest for subscribes in `config.json`.

After that, `public/v2sync/subscripts.txt`(default) will be generated.

Use Nginx or other file server to expose it.

Crontab may be useful. 

```crontab
0 7,19 * * * docker start stairspeedtest >/dev/null 2>&1
```


## Credits

- [tindy2013/stairspeedtest-reborn](https://github.com/tindy2013/stairspeedtest-reborn)

- [ShiroNekoWorks/v2sync](https://github.com/ShiroNekoWorks/v2sync)