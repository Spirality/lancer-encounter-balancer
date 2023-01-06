import zipfile as zf
import json


class LCP_Reader:
    def __init__(self, file) -> None:
        self.manifest = None
        # NPC Stuff
        self.npc_classes = None
        self.npc_features = None
        self.npc_templates = None

        # Player Stuff
        self.actions = None
        self.core_bonuses = None
        self.frames = None
        self.manufacturers = None
        self.mods = None
        self.statuses = None
        self.systems = None
        self.tags = None
        self.talents = None
        self.weapons = None

        # Not for mech encounters
        # self.backgrounds = None
        # self.environments = None
        # self.pilot_gear = None
        # self.reserves = None
        # self.sitreps = None
        # self.skills = None
        # self.tables = None

        with zf.ZipFile(file) as zip:
            # Read in the manifest and parse it.
            # Any failure means it's not a good LCP file,
            # but report what kind of problem was found.
            try:
                bytes = zip.read('lcp_manifest.json')
                self.manifest = json.loads(bytes)
            except json.JSONDecodeError as e:
                raise json.JSONDecodeError(
                    f'Error decoding the lcp_manifest file.') from e
            except ValueError as e:
                raise ValueError('Error: Zip file closed prematurely.') from e
            except KeyError as e:
                raise KeyError(
                    f"File {file} is not a valid Lancer LCP. No lcp_manifest.json found.") from e
            except:
                raise

            # NPC Stuff
            self.npc_classes = self.SafeLoad(zip, 'npc_classes.json')
            self.npc_features = self.SafeLoad(zip, 'npc_features.json')
            self.npc_templates = self.SafeLoad(zip, 'npc_templates.json')

            # Player Stuff
            self.actions = self.SafeLoad(zip, 'actions.json')
            self.core_bonuses = self.SafeLoad(zip, 'core_bonuses.json')
            self.frames = self.SafeLoad(zip, 'frames.json')
            self.manufacturers = self.SafeLoad(zip, 'manufacturers.json')
            self.mods = self.SafeLoad(zip, 'mods.json')
            self.statuses = self.SafeLoad(zip, 'statuses.json')
            self.systems = self.SafeLoad(zip, 'systems.json')
            self.tags = self.SafeLoad(zip, 'tags.json')
            self.talents = self.SafeLoad(zip, 'talents.json')
            self.weapons = self.SafeLoad(zip, 'weapons.json')

        pass

    def SafeLoad(self, zip, name):
        js = {}
        try:
            bytes = zip.read(name)
            js = json.loads(bytes)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f'Error decoding the {name} file.') from e
        except ValueError:
            raise ValueError('Error: Zip file closed prematurely.') from e
        finally:
            return js
