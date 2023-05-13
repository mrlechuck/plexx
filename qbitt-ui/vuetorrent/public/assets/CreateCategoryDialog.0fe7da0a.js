import{m as r,V as l}from "./vue.7fbf5199.js";import{a4 as c,a5 as _,a6 as m,Q as o,s as d,t as g,V as u,v as p,z as C,a as n,a3 as y,E as h,x as i}from "./index.83ab869a.js";import{M as v}from "./Modal.1c0dbfc6.js";import{_ as f}from "./VDialog.a8b9b171.js";import{_ as x}from "./VForm.85e44f31.js";import{_ as $}from "./VContainer.8c178cc9.js";const b={name:"CreateNewCategoryDialog",mixins:[v],props:{initialCategory:Object},data:()=>({category:{name:"",savePath:""},mdiCancel:c,mdiTagPlus:_,mdiPencil:m,valid:!1}),computed:{...r(["getSelectedCategory"]),hasInitialCategory(){return!!(this.initialCategory&&this.initialCategory.name)},nameRules(){return[s=>!!s||this.$t("modals.newCategory.tipOnNoName")]},PathRules(){return[s=>!!s||this.$t("modals.newCategory.tipOnNoPath")]}},created(){this.$store.commit("FETCH_CATEGORIES"),this.hasInitialCategory&&(this.category=this.initialCategory)},methods:{create(){o.createCategory(this.category),this.cancel()},cancel(){this.$store.commit("FETCH_CATEGORIES"),this.dialog=!1},edit(){o.editCategory(this.category),l.$toast.success(this.$t("toast.categorySaved")),this.cancel()}}};var w=function(){var t=this,a=t._self._c;return a(f,{attrs:{"content-class":"rounded-form","max-width":"300px"},model:{value:t.dialog,callback:function(e){t.dialog=e},expression:"dialog"}},[a(g,[a(u,{staticClass:"pa-0"},[a(p,{staticClass:"ma-4 primarytext--text"},[a("h3",[t._v(t._s(t.hasInitialCategory?t.$t("edit"):t.$t("createNew"))+" "+t._s(t.$t("category")))])])],1),a(C,[a(x,{ref:"categoryForm",staticClass:"px-6 mt-3",model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[a($,[a(n,{attrs:{rules:t.nameRules,label:t.$t("modals.newCategory.categoryName"),required:"",disabled:t.hasInitialCategory},model:{value:t.category.name,callback:function(e){t.$set(t.category,"name",e)},expression:"category.name"}}),a(n,{attrs:{rules:t.PathRules,label:t.$t("path"),required:""},model:{value:t.category.savePath,callback:function(e){t.$set(t.category,"savePath",e)},expression:"category.savePath"}})],1)],1)],1),a(y),a(h,{staticClass:"justify-end"},[t.hasInitialCategory?a(i,{staticClass:"accent white--text elevation-0 px-4",attrs:{disabled:!t.valid},on:{click:t.edit}},[t._v(" "+t._s(t.$t("edit"))+" ")]):a(i,{staticClass:"accent white--text elevation-0 px-4",attrs:{disabled:!t.valid},on:{click:t.create}},[t._v(" "+t._s(t.$t("create"))+" ")]),a(i,{staticClass:"error white--text elevation-0 px-4",on:{click:t.cancel}},[t._v(" "+t._s(t.$t("cancel"))+" ")])],1)],1)],1)},P=[],T=d(b,w,P,!1,null,null,null,null);const O=T.exports;export{O as default};
