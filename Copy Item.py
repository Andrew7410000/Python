def copy_item(target, source_item):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            item_properties = {}
            for property_name in ITEM_COPY_PROPERTIES:
                item_properties[property_name] = source_item[property_name]

            data_file = None
            
            if source_item.type in TEXT_BASED_ITEM_TYPES:
                # If its a text-based item, then read the text and add it to the request.
                text = source_item.get_data(False)
                item_properties['text'] = text
            
            elif source_item.type in FILE_BASED_ITEM_TYPES:
                # download data and add to the request as a file
                data_file = source_item.download(temp_dir)

            thumbnail_file = source_item.download_thumbnail(temp_dir)
            metadata_file = source_item.download_metadata(temp_dir)

            #find item's owner
            source_item_owner = source.users.search(source_item.owner)[0]
            
            #find item's folder
            item_folder_titles = [f['title'] for f in source_item_owner.folders 
                                  if f['id'] == source_item.ownerFolder]
            folder_name = None
            if len(item_folder_titles) > 0:
                folder_name = item_folder_titles[0]

            #if folder does not exist for target user, create it
            if folder_name:
                target_user = target.users.search(source_item.owner)[0]
                target_user_folders = [f['title'] for f in target_user.folders
                                       if f['title'] == folder_name]
                if len(target_user_folders) == 0:
                    #create the folder
                    target.content.create_folder(folder_name, source_item.owner)
            
            # Add the item to the target portal, assign owner and folder
            target_item = target.content.add(item_properties, data_file, thumbnail_file, 
                                             metadata_file, source_item.owner, folder_name)
            
            #Set sharing (privacy) information
            share_everyone = source_item.access == 'public'
            share_org = source_item.access in ['org', 'public']
            share_groups = []
            if source_item.access == 'shared':
                share_groups = source_item.groups
            
            target_item.share(share_everyone, share_org, share_groups)
            
            return target_item
        
    except Exception as copy_ex:
        print("\tError copying " + source_item.title)
        print("\t" + str(copy_ex))
        return None
