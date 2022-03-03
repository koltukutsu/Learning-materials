<template>
    <div v-if="list" class="nft-list-body">
        <div class="nft-holder"  v-for="nftObject in nftObjects" :key="nftObject.nftLabel">
            <nft-place-holder :nftObject="nftObject">
                <h2>{{ nftObject.nftLabel }}</h2>
            </nft-place-holder>
        </div>
    </div>
    <button @click="listNfts">{{ list }}</button>

</template>

<script>
import NftPlaceHolder from "./components/NftPlaceHolder.vue"

export default {
    components:{
    NftPlaceHolder,
    },

    data()  {
        return {
            list: false,
            nftObjects: [
                {
                    nftImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/moscow.svg',
                    nftLabel: "first"    
                },
                {
                    nftImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/paris1.svg',
                    nftLabel: "second"  
                },
                {
                    nftImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/rome.svg',
                    nftLabel: "third"  
                },
                {
                    nftImg: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/28963/paris2.svg',
                    nftLabel: "fourth"  
                },
            ],
        }
    },
    methods: {
        listNfts(){
            this.list = !this.list
        }
    }
}
</script>

<style>
body {
  width: 100vw;
  height: 100vh;
  font-family: 'NTR', sans-serif;
  background: #eee;
}   

.nft-holder{
  display: flex;  
  justify-content: center;
}
</style>