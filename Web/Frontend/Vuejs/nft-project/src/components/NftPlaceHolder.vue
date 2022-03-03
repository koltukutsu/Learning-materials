<template>
<div></div>
    <div class="nft-holder">
        <td>
        <slot></slot>
        <!-- <img :src="nftObject.nftImg"/> -->
        <img :src="nftObject.nftImg" widht="100" height="100"/>
        </td>
    </div>
</template>

<script>
export default {
    props: ["nftObject"]
}
</script>

 
<style lang="scss" scoped>
.nft-holder{
  display: flex;
  flex-direction: column;
  width: 280px;
  height: 320px;
  justify-content: center;
  background: white;
  border: 1px solid #ddd;
  padding: 20px 20px;
  margin: 10px;
  h2 {
    margin: 0;
    text-align: center;
  }
  img {
    margin: 10px;
    align-self: center;
  }
}
</style>