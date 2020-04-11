from  Cryptodome.Cipher  import  AES
from  Cryptodome  import  Random

ciphertext = bytes.fromhex("f83b03173b7e17068f3c7b03624cbcace28ecdb93a5535e3961890443b58337419cb6cfab396ea3206ec0d5fcdf8b7bd5cb791df4f5b15a81ade19eac277470944d5ba8c957f045b5ce83483fa9d6ce5c1b2fd106f4a124b671d6a250f35ca01045fb35b9d53c1319001eb89be43e28a90a914ce6c44609d856fc8e0d2a5dce5a4945964e3b0dddfa42826c695190c267bbf1a10f4667b6cee885f2d43e1f5b89f04ccc0a8fecc5cc6bd5f20af1983cdf1c275ac66caf0b831c1259b0578a00576120abf6fad8817776f1ecf33c8cff8ef853c29351cf424b16eaf670b8e901804a092ec35c8491b90d8f3b7b8a52a281287fc9bf9d1c987cf515526cd02f88ffcd04ec70080e6ddeae5ea7a5737b8b2e64072403fe686e86c7dd3ace8cf361038cdbc05bf1dd0e39d5bfc345e2fce9d9e982243e8d15838f458a33b23c1bfac5a924dae2f933e8e0466427394e2933e5be362a84530d87171781cd9f9154e0b904307488b140667bba76314851e307e519901001f9816d4fc3191deba3ea56e174438c35c9c4e724b109569da12b4ca69a1e1410541c3acc375a46f498ea22b40ba8bd53ae089355654814ec719a34215c958ce0d1f9925f6506a0177c78742d93c52dce8569878a232937b69848958cea642d05efd488b8af612187a9546d2f2a2c9d5c1f45ec87d6ab51a12b1a5aa1ff5bcdb40ef8810579509d3054da7b431d350fff46c4fd6ad1d79baffeaef471106b6d232158741705880a66d116baebd89e92e216c1b2e929b7021f999ec47e79dc076351ef5e461306377f0365c8c4aad4d11ee98d68a13e1792a31b2ff0f4b0c1c31c43e1eb3099c04b31473b6992c68afd013f5e0a8af064d050d38878d482a0d837d4618fcd3272316ee379f37530707211bb0047cc5f0fa296dd4688e92f042cbde9afca4b4222a0bd5ecf37579d012f8228b47ba74f16f3b436c6ca20ea5a4e16996a1a1207f35da2754a111e3b9ed8888c24c544277bdff1733a343259cc433dad85fb6667953344a50244bdf8411fe01fa8119be00b4b27fa132df11705389cf99791e99b7d85892a7163ea5dd7e57494f6a907655fdb5e265543e659c6143719afe77195774f56bd9d5a74003a517e6889d315bfe15b7838fd656d3482483d85e4729c25e18787cdca00ea576368978ac954c97e889874bfb9abb2a9038b0dba65921221c3786f467de8a777075ad398c74aa2f8f590f3e23a445cc199b639f936")

key = bytes.fromhex("6555d417a283161f440cfad518eb852845a6ff45f7e1b7623090b7714a5bbd5f")

iv = bytes.fromhex("9e6632df5a211060622769d9c2300753")

aes = AES.new(key , AES.MODE_CFB , iv)


plaintext = aes.decrypt(ciphertext)

print(plaintext)