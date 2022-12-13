<template>
 <div>{{BASE_URL}}</div>
</template>

<script async lang="ts" setup>

const BASE_URL = process.env.NODE_HOST
</script>