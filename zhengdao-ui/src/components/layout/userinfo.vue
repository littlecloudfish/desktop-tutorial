<template>
    <div>
        <el-row class="infocard">
            <el-col :span="200">
                <el-image style="width: 150px; height: 150px" src="https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg" fit="fill" />
            </el-col>
            <el-col :span="12" class="textinfo">
                <p style = "color:white">Player Name:{{userinfomation.fullname}}</p>
                <p style = "color:white">Player DiscordId:{{userinfomation.discordId}}</p>
                <p style = "color:white">Account Created Day:{{userinfomation.create_date}}</p>
            </el-col>
            
        </el-row>
        <div v-if="dataready">
            <!-- <div> -->
                <!-- <display-music :posts=userpublish></display-music> -->
            </div>
        <el-row>
        
        </el-row>   
    </div>
</template>

<script lang="ts" setup>
const userinfomation = {fullname:'hello fucker', create_date:'hello date', discordId :'9001'};
const dataready = false



</script>


 

  <style scoped>
 .infocard{
    border-radius: 18px;
    padding-bottom: 3%;
    background:#0f2743;
  } 
  .el-image{
    padding-top:20%;
    padding-left:10%;
  }
  .textinfo{
    padding-left:50px;
    padding-top:3%;
  }
  
  </style>