from Cryptodome.Hash import SHA256

hex_hash = SHA256.new(b"Hello  world!").hexdigest()

incremental_hash = SHA256.new()
incremental_hash.update(b"Hello")
incremental_hash.update(b"world!")
print(incremental_hash.hexdigest())


#bin_hash = SHA256.new(b"Hello  world!").digest()
#printable = bin_hash.hex()
#print(printable)